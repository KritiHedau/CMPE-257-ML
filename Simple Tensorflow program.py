# addition of two tensors (constants)
Run Command Prompt as Administrator(For Windows)
C:\WINDOWS\system32>python
Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import tensorflow as tf
>>> a=tf.constant(3)
>>> b=tf.constant(2)
>>> c=a+b
>>> sess=tf.Session()
>>> print(sess.run(c))

Output- 5
