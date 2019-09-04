
const axios = require('axios')
const url = 'https://api.telegram.org/bot801847892:AAHCc2UY3PEie96sc_PwpeMN5yq2aZTaADM/sendMessage?chat_id=858314777&text=자바스크립트메세지'

axios.get(url)
    . then((res) => {
        console.log(res)
    })