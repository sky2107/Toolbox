> Creating image for Python flask application <br>

> FROM ubuntu:14.04 <br>
> RUN apt-get install -y python <br>
> RUN apt-get install -y python-pip <br>
> RUN apt-get clean all <br>
> <br>
> RUN pip install flask <br>
> <br>
> ADD hello.py /tmp/hello.py
> <br>
> EXPOSE 5000 <br>
> CMD ["python", "/tmp/hello.py"] <br>

> To cop the application inside the container we use the ADD command.

> BAD practice above

> Instead to this <br>
> FROM ubuntu:14.04 <br>
> RUN apt-get update && install -y \ <br>
>   python <br>
>   python-pip <br>
> RUN pip install flask <br>
> COPY hello.py /tmp/hello.py <br>
> ...

> AND even better USE official tag of python:2.7

> FROM python:2.7 <br>
> RUN pip install flask <br>
> COPY hello.py /tmp/hello.py
> ...

