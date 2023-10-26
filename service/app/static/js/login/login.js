(function (message) {

    function switchToDashboard() {
        window.location.href = "/"
    }

    function checkSession() {
        const accessToken = localStorage.getItem(ACCESS_TOKEN_KEY);
        console.log(accessToken)
        if (accessToken !== null) {
            switchToDashboard()
        }
    }


    checkSession()

    document.getElementById('button-login').addEventListener('click', function (e) {
        e.preventDefault();
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        const data = {
            username: username,
            password: password
        };

        fetch('/auth/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
            .then(response => {
                return response.json();
            })
            .then(data => {
                if (data.status === 401){
                    alert(data.message)
                }
                else {
                    localStorage.setItem(ACCESS_TOKEN_KEY, data.data.accessToken);
                    switchToDashboard()
                }

            })
            .catch(error => {
                console.log('Error:' + error);
            });
    });

})()