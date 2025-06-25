let http = require('http');

http.createServer(function(req, res) {
    res.writeHead(200, {'content-type': 'text/html'});
    res.end('Hello rifatbroh');
}).listen(8080);