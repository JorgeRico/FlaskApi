# Flask api
Flask demo api with swagger

#### Build
```bash
 - docker build --tag python-docker .
```

#### Run
```bash
 - docker run -d -p 5000:5000 python-docker
```

#### Swagger
```bash
 - http://localhost:5000/
```

#### Endpoints
```bash
 - GET    http://localhost:5000/books
 - GET    http://localhost:5000/books/1
 - POST   http://localhost:5000/books
 - PUT    http://localhost:5000/books/1
 - DELETE http://localhost:5000/books/1
```
