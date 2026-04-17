import 'package:flutter/material.dart';
import 'package:flutter_tts/flutter_tts.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() => runApp(TranslationApp());

class TranslationApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Machine Translation',
      theme: ThemeData(
        primarySwatch: Colors.blue, // MaterialColor for primarySwatch
        primaryColor: Color.fromARGB(255, 8, 133, 236), // Custom primary color
      ),
      home: TranslationHomePage(),
    );
  }
}

class TranslationHomePage extends StatefulWidget {
  @override
  _TranslationHomePageState createState() => _TranslationHomePageState();
}

class _TranslationHomePageState extends State<TranslationHomePage> {
  final TextEditingController _inputController = TextEditingController();
  String _outputText = "";
  String _sourceLanguage = "en";
  String _targetLanguage = "ar";
  final FlutterTts flutterTts = FlutterTts();

  Future<void> translateText() async {
    String inputText = _inputController.text;

    if (inputText.isEmpty) {
      setState(() {
        _outputText = "Please enter some text.";
      });
      return;
    }

    // API Call to Translation Backend (replace with your API URL)
    try {
      final response = await http.post(
        Uri.parse('http://192.168.1.171:8000/translate'),  // Use your FastAPI backend URL here
        headers: {'Content-Type': 'application/json'},
        body: json.encode({
          'text': inputText,
        }),
      );

      if (response.statusCode == 200) {
        final data = json.decode(response.body);
        setState(() {
          _outputText = data['translated_text'] ?? "Translation failed.";
        });
      } else {
        setState(() {
          _outputText = "Error: Unable to fetch translation.";
        });
      }
    } catch (e) {
      setState(() {
        _outputText = "Error: $e";
      });
    }
  }

  void playOutputText() async {
    await flutterTts.setLanguage(_targetLanguage);
    await flutterTts.speak(_outputText);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('English to Arabic Translation'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            // Input Text
            TextField(
              controller: _inputController,
              decoration: InputDecoration(
                border: OutlineInputBorder(),
                labelText: 'Enter text to translate',
              ),
              maxLines: 3,
            ),
            SizedBox(height: 16),

            // Language Selection (Optional, depending on your use case)
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                DropdownButton<String>(
                  value: _sourceLanguage,
                  items: [
                    DropdownMenuItem(value: 'en', child: Text('English')),
                    DropdownMenuItem(value: 'ar', child: Text('Arabic')),
                  ],
                  onChanged: (value) {
                    setState(() {
                      _sourceLanguage = value!;
                    });
                  },
                ),
                DropdownButton<String>(
                  value: _targetLanguage,
                  items: [
                    DropdownMenuItem(value: 'ar', child: Text('Arabic')),
                    DropdownMenuItem(value: 'en', child: Text('English')),
                  ],
                  onChanged: (value) {
                    setState(() {
                      _targetLanguage = value!;
                    });
                  },
                ),
              ],
            ),
            SizedBox(height: 16),

            // Translate Button
            ElevatedButton(
              onPressed: translateText,
              child: Text('Translate'),
            ),
            SizedBox(height: 16),

            // Output Text
            Text(
              _outputText,
              style: TextStyle(fontSize: 18, color: Colors.black),
            ),
            SizedBox(height: 16),

            // Play Translated Text
            ElevatedButton.icon(
              onPressed: playOutputText,
              icon: Icon(Icons.volume_up),
              label: Text('Play Translation'),
            ),
          ],
        ),
      ),
    );
  }
}
