# Albumy

*Capture and share every wonderful moment.*

> Example application for *[Python Web Development with Flask](https://helloflask.com/en/book/1)* (《[Flask Web 开发实战](https://helloflask.com/book/1)》).

Demo: http://albumy.helloflask.com

![Screenshot](https://helloflask.com/screenshots/albumy.png)

## Installation

clone:
```
$ git clone https://github.com/danyatingshen/albumy.git
$ cd albumy
```
Install/update to the correct python version: see here for more instruction https://www.dataquest.io/blog/installing-python-on-mac/
```
$ python --version 
Python 3.10.9
```
create & activate virtual env then install dependency:

with venv/virtualenv + pip:
```
$ python -m venv env  # use `virtualenv env` for Python2, use `python3 ...` for Python3 on Linux & macOS
$ source env/bin/activate  # use `env\Scripts\activate` on Windows
$ pip install -r requirements.txt
```
or with Pipenv:
```
$ pipenv install --dev
$ pipenv shell
```
generate fake data then run:
```
$ flask forge
$ flask run
* Running on http://127.0.0.1:5000/
```
Test account:
* email: `admin@helloflask.com`
* password: `helloflask`


## API creditials
- Create your Azure Computer vision instance by following step here: https://www.youtube.com/watch?v=1VB_QrHm_nY
- Cretae `secrete.json` file in this path with this path `albumy/blueprints/secrete.json` so it can read here https://github.com/danyatingshen/albumy/blob/606f97283163b4fc1b5f89bad9675650fa88bc0c/albumy/blueprints/alternative.py#L9. The format of the secrete should be 
```
{
  "API_KEY": "your key",
  "END_POINT": "your endpoint"
}
```
so that it can be parse correctly here https://github.com/danyatingshen/albumy/blob/606f97283163b4fc1b5f89bad9675650fa88bc0c/albumy/blueprints/alternative.py#L10-L11


## License

This project is licensed under the MIT License (see the
[LICENSE](LICENSE) file for details).
