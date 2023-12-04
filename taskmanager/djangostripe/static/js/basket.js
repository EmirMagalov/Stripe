card=document.querySelectorAll(".basketblock")
n=0
card.forEach(f=>{
total=f.querySelector(".totalprice").innerText=(f.querySelector(".basketcount").innerText * f.querySelector(".basketprice").innerText).toFixed(2)
n=n+parseFloat(total)
})
document.querySelector(".alltotal").innerText=n
//document.querySelector(".totalinput").value=n



var handler = StripeCheckout.configure({
key: 'pk_test_51OI8b2FVjktvFpLStcKQP80WUGw6DNIwlQlNl1Ujvztp2f3hhPHOATQ9axz7IMqbZbS9GT63ruDlAatUiZ5ngdQ0008csksUKO',
locale: 'auto',
token: function(token) {


sendTokenToServer(token);
}
});

document.getElementById('custom-pay-button').addEventListener('click', function() {
handler.open({
name: 'Your Company Name',
description: 'Description of your product or service',
currency: 'usd',
amount: parseFloat(document.querySelector(".alltotal").innerText)*100,
});
});

window.addEventListener('popstate', function() {
  handler.close();
});
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

function sendTokenToServer(token) {
  fetch('/check', {
    method: 'POST',
    headers: {
      'X-CSRFToken': csrftoken,
    },
    body: JSON.stringify({
      token: token.id,
      amount:parseFloat(document.querySelector(".alltotal").innerText),
      description: 'Your product or service description'

    })
  })
.then(response => {
    // Проверка успешности HTTP-статуса
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    // Если ответ успешен, вы можете обработать данные ответа
    window.location.reload()
    return response.json();
  })

}

