const axios = require('axios')


url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=874'
    axios.get(url) 
    .then((res) => {
        let winner = []
        winner.push(res,data.drwtNo1)
        winner.push(res,data.drwtNo2)
        winner.push(res,data.drwtNo3)
        winner.push(res,data.drwtNo4)
        winner.push(res,data.drwtNo5)
        winner.push(res,data.drwtNo6)
    })