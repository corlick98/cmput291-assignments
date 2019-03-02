test: main.py printoptions.py
	cat main.py printoptions.py >|test.py

clean:
	rm -f test.py