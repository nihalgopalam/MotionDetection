function example(){
    document.getElementById("demo").innerHTML = "Paragraph changed.";
}

function login(){
    var user = document.getElementById("UserID").value;
    var userPattern = /^.{6,}$/;

    var pass = document.getElementById("Password").value;
    var passPattern = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{6,}$/;


    if (!(userPattern.test(user))){
        var userAlert = "Username: minimum 6 characters";
        document.getElementById("loginAlert").innerHTML = '<div id="alert" class="alert alert-warning alert-dismissible fade" role="alert"> ' + userAlert + '<button type="button" class="btn-close" data-dismiss="alert" aria-label="Close"></button> </div>';
    }
    else if(!(passPattern.test(pass))){
        var passAlert = "Password: minimum 6 characters. Must include a letter, a number, and a special character";
        document.getElementById("loginAlert").innerHTML = '<div id="alert" class="alert alert-danger alert-dismissible fade" role="alert"> ' + passAlert + '<button type="button" class="btn-close" data-dismiss="alert" aria-label="Close"></button> </div>';
    }
    


    var bsAlert = new bootstrap.Alert(document.querySelector("#alert"));
    setTimeout(() => {
        bsAlert.close();
    }, 1000);

    $(document).ready(function(){
        alert("jQuery is working")
    });


}

function success_login(){
    var user = document.getElementById("UserID");
    var pass = document.getElementById("Password");

    var login_data = [
        {"UserID": user},
        {"Password": pass}
    ];

    $.ajax({
        type: "POST",
        url: "/login_process",
        data: JSON.stringify(login_data),
        contentType: "application/json",
        dataType: 'json' 
      });
}



