/*

1부터 45까지 숫자 중 6개 비복원 추출
> [2,5,34,12,23,11]

(힌트) lodash 활용하면 쉽다

*/

const _ = require('lodash')

// 1. 1~45까지 담긴 동 생성

const numbers = _.range(1,46)

// 2, 랜덤으로 6개 출력

console.log(_.sampleSize(numbers,6))

// 3. 정렬

console.log(_.sortBy(_.sampleSize(numbers,6)))


//  winner와 로또를 비교해서 몇개가 일치하는지 그리고 몇등인지 출력
// 6개 ,1등
// 5개, 3등
// 4개, 4등
// 3개, 5등

// const winner = [1,5,19,23,28,42]
// const lotto = _.sortBy(_.sampleSize(numbers,6))

// if (_.isEqual(winner, lotto)) {
//     console.log("6개, 1등");
// }
    
// else if (_.without(winner,lotto) = _.sampleSize = 1) {
//  console.log("5개, 3등");
// }

// else if (_.without(winner,lotto) = _.sampleSize = 2 ) {
//     console.log("4개, 4등");
// }

// else if ( _.without(winner,lotto) = _.sampleSize = 3) {
//     console.log("3개, 5등");
// }
// else   

// console.log("2개, 꽝");


const cnt = _.intersection(lotto,winner).length
console.log 

if  (cnt == 1) {
    rank = 1등입니다}


lotto .forEach(function(num) {
    if (winner.includes(num)) {
        cnt += 1;
    }
})


