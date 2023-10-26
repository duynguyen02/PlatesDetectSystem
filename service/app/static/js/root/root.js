const DASHBOARD_ELEMENTS = [
    "licensePlateManagement",
    "inOutHistory"
]

function switchToLogin() {
    localStorage.removeItem(ACCESS_TOKEN_KEY)
    window.location.href = "/login"
}

function openDashboard(dashboard) {
    DASHBOARD_ELEMENTS.forEach((e) => {
        document.getElementById(e).style.display = 'none';
    })
    document.getElementById(dashboard).style.display = 'block';
}

function loadApprovedPlates() {
    openDashboard('licensePlateManagement')
    fetchApprovedPlates(localStorage.getItem(ACCESS_TOKEN_KEY))
}

function addLicensePlate(licensePlate, date) {
    var table = document.getElementById('licensePlateTable');
    var row = table.insertRow(-1);
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    var cell3 = row.insertCell(2);
    cell1.innerHTML = licensePlate;
    cell2.innerHTML = date;
    cell3.innerHTML = '<button class="btn btn-danger btn-sm" onclick="openModal(this)">Xóa</button>';
}

function requestAddNewPlate() {

    var licensePlate = document.getElementById('licensePlate').value;

    var myModal = bootstrap.Modal.getInstance(document.getElementById('addModal'));
    myModal.hide();

    var myHeaders = new Headers();
    myHeaders.append("Authorization", `Bearer ${localStorage.getItem(ACCESS_TOKEN_KEY)}`);
    myHeaders.append("Content-Type", "application/json");

    var raw = JSON.stringify({
        "plate": licensePlate
    });

    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };

    fetch("/approved_plates", requestOptions)
        .then(response => response.json())
        .then(result => {
            if (result.status === 401) {
                switchToLogin()
            }
            fetchApprovedPlates(localStorage.getItem(ACCESS_TOKEN_KEY))
        })
        .catch(error => console.log('error', error));
}

function fetchApprovedPlates(token) {
    clearAllRecord()
    var table = document.getElementById('licensePlateTable');
    // table.innerHTML = ""
    const myHeaders = new Headers();
    myHeaders.append("Authorization", `Bearer ${token}`);

    const requestOptions = {
        method: 'GET',
        headers: myHeaders,
        redirect: 'follow'
    };

    fetch("/approved_plates", requestOptions)
        .then(response => response.json())
        .then(result => {
            if (result.status === 401) {
                switchToLogin()
            }
            result.data.forEach((e) => {
                addLicensePlate(e.plate, new Date(e.create_at).toString())
            })
        })
        .catch(error => {
            console.log(error)
        });
}

var myModal = new bootstrap.Modal(document.getElementById('changePasswordModal'));

function openChangePasswordModal() {
    myModal.show();
}

function changePassword() {
    var newPassword = document.getElementById('newPasswordInput').value;
    var confirmPassword = document.getElementById('confirmPasswordInput').value;

    if (newPassword === confirmPassword) {
        var url = '/auth/change_password';
        var token = localStorage.getItem(ACCESS_TOKEN_KEY);
        var myHeaders = new Headers();
        myHeaders.append("Content-Type", "application/json");
        myHeaders.append('Authorization', 'Bearer ' + token);
        var raw = JSON.stringify({
            "password": newPassword
        });

        var requestOptions = {
            method: 'POST',
            headers: myHeaders,
            body: raw,
            redirect: 'follow'
        };

        fetch("/auth/change_password", requestOptions)
            .then(response => response.json())
            .then(result => {
                if (result.status === 401) {
                    switchToLogin()
                }
                if (result.status === 200) {
                    alert("Đổi mật khẩu thành công");
                    myModal.hide();
                }
                else {
                    alert(result.message);
                }
            })
            .catch(error => console.log('error', error));

    } else {
        alert("Mật khẩu xác nhận không khớp");
    }
}

function logout(){
    localStorage.removeItem(ACCESS_TOKEN_KEY)
    switchToLogin()
}

function clearAllRecord() {
    var table = document.getElementById("licensePlateTable");
    var rowCount = table.rows.length;
    for (var i = 1; i < rowCount; i++) {
        table.deleteRow(1);
    }
}
