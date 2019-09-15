function address_red(type_of_server) {
    if (type_of_server === 'original'){
        return "https://projects.osinit.com"
    } else if (type_of_server === 'test'){
        return "http://85.234.37.158:45456"
    } else {
        return "http://192.168.111.74:3718"
    }
}

url_red = address_red("test");