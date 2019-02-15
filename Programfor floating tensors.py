C:\WINDOWS\system32>python
>>> import tensorflow as tf
>>> a=tf.placeholder(tf.float32)
>>> b=tf.placeholder(tf.float32)
>>> c=a+b
>>> sess=tf.Session()
>>> print(sess.run(c,{a:5,b:6}))


OUTPUT -11.0
