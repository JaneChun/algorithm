process.stdin.setEncoding('utf8');
process.stdin.on('data', data => {
    console.log(('*'.repeat(+data.split(' ')[0]) + '\n').repeat(+data.split(' ')[1]));
});