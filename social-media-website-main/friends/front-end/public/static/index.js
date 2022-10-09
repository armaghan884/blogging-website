function userCreate() {

    console.log("userCreate()");
    const name = document.getElementById("name").value;
    const user_name = document.getElementById("validationDefaultUsername").value;
    const date_of_birth = document.getElementById("datepicker").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const phone = "1234567890"
    const gender = "M";
    const street_name = "Bexter Avenue";
    const street_number = 123;
    const city = document.getElementById("city").value;
    const post_code = "75123000";
    const country = document.getElementById("country").value;

    const xhttp = new XMLHttpRequest();
    xhttp.open("PUT", "http://127.0.0.1:5000/v1/user");
    xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhttp.send(JSON.stringify({ 
      "name": name, "user_name": user_name, "email": email, "phone": phone,
      "gender": gender, "password": password, "date_of_birth": date_of_birth, 
      "street_name": street_name, "street_number": street_number, "city": city, "post_code": post_code,
      "country": country
    }));
}