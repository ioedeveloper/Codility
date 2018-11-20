solution = (N) => {
    // write your code in ES6
    if(N < 1){
        return 0;
    }else{
        let strNum = N.toString();
        let strBinary = (+strNum).toString(2);
        savedGap = [];
        countGap = 0;
        start = 0;
        for(i of strBinary){
            if(start==0){
                start = parseInt(i);
            }else if(start == 1 && parseInt(i) == 0){
                countGap +=1;
            }else if(start == 1 && parseInt(i) == 1){
                start = 1;
                savedGap.push(countGap);
                countGap = 0;
            }
        }
        if(savedGap.length < 1) return 0;
        return Math.max(...savedGap);
    }
}

console.log(solution(32))