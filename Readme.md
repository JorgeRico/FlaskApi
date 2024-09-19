###### create image
docker build --tag python-docker .

###### run
docker run -d -p 5000:5000 python-docker
