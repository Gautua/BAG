window.onload=function() {
// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyAPXfhz5baCzi4k09AuuiCqrWP7eSAIdPk",
  authDomain: "data-cleaning-1576596024579.firebaseapp.com",
  databaseURL: "https://data-cleaning-1576596024579.firebaseio.com",
  projectId: "data-cleaning-1576596024579",
  storageBucket: "data-cleaning-1576596024579.appspot.com",
  messagingSenderId: "604168784817",
  appId: "1:604168784817:web:0ffe7612683545880d0b90",
  measurementId: "G-MBLH2XQ6Y9"
};

  //initialize the firebase
  firebase.initializeApp(firebaseConfig);

// Get Elements
// Login
const user_login=document.getElementById('username_login');
const password_login=document.getElementById('password_login');
const btnLogin=document.getElementById('signinbutton')
const btnLogout=document.getElementById('btnLogout')
//sign-up
const user_signup=document.getElementById('Email_signup');
const password_signup=document.getElementById('Password_signup');  
const btnSignUp=document.getElementById('signup_btn')

// send values to the firebase once a button is clicked
btnLogin.addEventListener('click', e => {
  const email=user_login.value;
  const pass=password_login.value;
  const auth=firebase.auth();
  //sign in
  const promise=auth.signInWithEmailAndPassword(email,pass);
  promise.catch(e=>console.log(e.message));

  
});

btnSignUp.addEventListener('click',e=>{
  const email_s=user_signup.value;
  const pass_s=password_signup.value;
  const auth=firebase.auth();
  //sign in
  const promise=auth.createUserWithEmailAndPassword(email_s,pass_s);
  promise
  .catch(e=>console.log(e.message));
  
});
btnLogout.addEventListener('click',e=>{
firebase.auth().signOut();
});
firebase.auth().onAuthStateChanged(firebaseUser=> {
if(firebaseUser){

  console.log(firebaseUser);
  btnLogout.classList.remove('hide');
  //window.open('/upload_file')
  //Try Here------------------------------------------------------------<<<<< 
}
  else
  {
    console.log('not logged in');
    btnLogout.classList.add('hide');
  }
});
};