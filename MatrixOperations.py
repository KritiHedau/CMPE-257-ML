C:\WINDOWS\system32>python
>>> import tensorflow as tf
>>> # USING MATRIX AS INPUT AND PERFORMING OPERATIONS ON THAT
...
>>> a=tf.placeholder(tf.float32, shape=(2,1))
>>> b=tf.placeholder(tf.float32, shape=(1,2))
>>> # Here, a is 2D matric with 2 rows 1 column
...
>>> #and b is also matrix with 1 row 2column
...
>>> c=tf.matmul(a,b)
>>> sess=tf.Session()
>>> print(sess.run(c,{a:[[1],[2]],b:[[3,4]]}))

Output - [[3. 4.]
 [6. 8.]]
