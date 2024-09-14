# Django
![image](https://github.com/user-attachments/assets/502e4f2d-4ccf-44d5-8ba8-d17f02442a33)

Django signals are executed synchronously by default.
When a signal is sent, its corresponding receivers (signal handlers) are executed immediately and sequentially, meaning that they block the flow of the program until they finish executing.
code:

https://github.com/ashilmathew/Django/blob/main/q1.py

![image](https://github.com/user-attachments/assets/ded12a35-5af7-4be2-b0ee-f1995a007044)

Yes, Django signals run in the same thread as the caller by default.
Django signals are executed synchronously in the same thread that sent them unless explicitly configured otherwise. This means that if a signal is sent during a request, the signal handler will run in the same thread handling that request.

code:

https://github.com/ashilmathew/Django/blob/main/q2.py

By default, Django signals do not run in the same database transaction as the caller.
This means that if an exception occurs in a signal handler, it will not automatically cause the surrounding database transaction to be rolled back, unless explicitly handled.
If you want a signal to participate in the same database transaction as the caller, you need to wrap the signal handler logic inside a database transaction using transaction.atomic().

code:

https://github.com/ashilmathew/Django/blob/main/q3.py
