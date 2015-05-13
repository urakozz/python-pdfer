# pdfer

## installation

install python, pip
```
sudo pip install virtualenv
cd <project>
virtualenv env
env/bin/pip install -r requirements.txt 
```

## misc

https://github.com/ddollar/heroku-buildpack-multi

https://github.com/urakozz/heroku-buildpack-imagemagick-cedar-14
https://github.com/thenovices/heroku-buildpack-scipy

```
brew install ghostscript imagemagick
```
```
sudo pkill gunicorn
gunicorn pdfer.wsgi --bind 127.0.0.1:8000 --daemon --log-level=debug --log-file=gunicorn.log --timeout=600
```
