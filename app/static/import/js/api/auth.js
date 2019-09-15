// data = JSON.stringify ( {login: "admin", password: "P@ssword123", domain: "http://192.168.111.74:3718"} );
// fff = JSON.parse ( data );

jQuery ().ready ( function () {
    const url = location.protocol + "//" + location.host;
    console.log ( $.cookie ( 'api_key' ) );

    if ($.cookie ( 'api_key' ) != null) {
        console.log ( $.cookie ( 'api_key' ) );
        window.location.replace(url + '/web/main/');
        //window.location.href = 'main/';
    } else {


        $ ( '.btn' ).on ( 'click', function () {
            if ($.cookie ( 'api_key' ) == null) {
                let s = JSON.stringify ( {
                    login: $ ( ".login" ).val (),
                    password: $ ( ".password" ).val (),
                    // domain: $("#domain").val()
                    domain: url_red
                } );

                $.ajax ( {
                    url: url+'/api/',
                    type: 'POST',
                    data: s,
                    dataType: "text",
                    success: function (data) {
                        json_data = JSON.parse(data);
                        if ($ ( '#exampleCheck1' ).is ( ':checked' )) {
                            $.cookie ( 'api_key', json_data.api_key, {expires: 80, path: '/'} );
                            $.cookie ( 'name', json_data.name, {expires: 80, path: '/'} );
                            console.log ( data );
                            window.location.replace(url + '/web/main/');
                            // window.location.href = 'main/';
                        } else {
                            $.cookie ( 'api_key', json_data.api_key, {expires: 1, path: '/'} );
                            $.cookie ( 'name', json_data.name, {expires: 1, path: '/'} );
                            console.log ( data );
                            window.location.replace(url + '/web/main/');
                            // window.location.href = 'main/';
                        }
                    }
                } );
            } else {

            }
        } );
    }

    //for (let key in fff) $ ( "#" + key + "" ).html ( fff[key] );


} );
