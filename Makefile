test: main.py q1.py q2.py q3.py q4.py q5.py q6.py printoptions.py
	cat main.py q1.py q2.py q3.py q4.py q5.py q6.py printoptions.py>|assignment3.py

clean:
	rm -f assignment3.py
