
const url = location.protocol + "//" + location.host;

const user_card = post => {
    return `
        <div class="account-user">
            <img class="photo-user" src=""
                 alt="logo">
            <div class="user-information">
                <div class="name-user">${post.name}</div>
                <div class="user-position">${post.roles.join ( ', ' )}</div>
            </div>
        </div>
    `
};
const project_card = post => {
    return `
        <li><a href="#" class="project1" id="${post.id}">${post.name}</a></li>
    `
};


function trace_array(type_info, data) {
    const $posts = document.querySelector ( '#' + type_info );
    let html = '';
    if (data.length) {
        if (type_info === 'members') {
            html += data.map ( post => user_card ( post ) ).join ( ' ' );
        } else {
            html += data.map ( post => project_card ( post ) ).join ( ' ' );
        }
    } else {
        html += `<h2 class="center">...no ` + type_info + `...</h2>`
    }
    $posts.innerHTML = html;
    $ ( '.project1' ).on ( 'click', function () {
        pr = $ ( this ).attr ( 'id' );
        console.log(pr);
        if (pr != null) {
            $('.project-name').html($(this).text());
            $('title').html($(this).text());
            get_info ( 'members', pr );
        }
    } );
}


function get_info(type_info, project_id) {
    let s;
    if (project_id != null) {
        s = JSON.stringify ( {
            key: $.cookie ( 'api_key' ),
            url_r : url_red,
            project_id: project_id,
        } );
    } else {
        s = JSON.stringify ( {
            key: $.cookie ( 'api_key' ),
            url_r : url_red
        } );
    }

    $.ajax ( {
        url: url + '/api/load_' + type_info + '/',
        type: 'POST',
        data: s,
        dataType: "text",
        success: function (data) {
            if (data !== null) {
                console.log(data);
                trace_array ( type_info, JSON.parse ( data ) );
                console.log ( 'норм всё' );
            } else {
                // $ ( '.end' )
                //     .addClass ( 'alert-danger' )
                //     .show ( 400 )
                //     .html ( 'не отправлено' );
                // setTimeout ( function () {
                //     $ ( '.end' ).hide ( 100 );
                // }, 3000 );
                console.log ( 'что-то там не так' );
            }
        }
    } );
}





