########## MrayS -> Multiple Rays tracer #############

Was ist MrayS ?
 
	MrayS ist ein Renderprogramm das in Python geschrieben wurde


Was für Softwarepakete braucht man für MrayS ?

	-Python
	-Python Imaging Library (PIL)/Pillow Library


Welche Formate werden benutzt
	
	*.raw - für 3D Szenen
	*.jpg - für gerenderte Bilder  

Wie benutzt man MrayS

	Das Hauptprogramm wird auf Linuxsystemen aufgerufen indem man
		python MrayS.py
	aufruft. Allerdings muss man noch eine Szene und eine Auflösung spezifizieren.
		python MrayS.py ball_plane.raw 1920 1080

Wie kann man den Renderprozess beschleunigen ?

	- einen schnelleren Prozessor verwenden
	- pypy, einen alternativen Python Interpreter benutzen, der mathematische Operationen schneller durchführt
		python MrayS.py ball_plane.raw 1920 1080 -pypy




