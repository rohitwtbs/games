(function() {
    // your page initialization code here
    // the DOM will be available here
    if(document.readyState === 'complete'){
        main();
    }
   
 
 })();

 let state = [[0,0,0],[0,0,0],[0,0,0]]

 function main() {
    let gameBoard = document.getElementById('gameBoard');
    gameBoard.addEventListener('click', (e) => {
        s = e.target;
        s.innerHtml = 'X';
        console.log(s.id);
        console.log(s.innerHtml);
    })
 }