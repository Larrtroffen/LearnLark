<template>
    <div id="form-ui">
      <form action="" method="post" id="form">
        <div id="form-body">
          <div id="welcome-lines">
            <div id="welcome-line-1">LearnLark</div>
            <div id="welcome-line-2">开始你的学习之旅！</div>
          </div>
          <div id="input-area">
            <div class="form-inp">
              <input placeholder="邮箱地址" type="email">
            </div>
            <div class="form-inp">
              <input placeholder="密码" type="password">
            </div>
            <div class="form-inp">
              <input placeholder="确认密码" type="password">
            </div>
          </div>
          <div id="submit-button-cvr">
            <button id="submit-button" type="submit">注册</button>
          </div>
          <div id="forgot-pass">
            <a href="#">已有账号？点击这里登陆</a>
          </div>
        </div>
      </form>
    </div>
  </template>
  
  <style scoped>
  #form {
    display: grid;
    place-items: center;
    width: 300px;
    height: auto;
    padding: 25px;
    background-color: #ffffffcb;
    box-shadow: 0px 15px 60px #55ACEE;
    outline: 1px solid #44AAFF;
    border-radius: 20px;
  }
  
  #form-body {
    display: grid;
    position: center;
  }
  
  #welcome-lines {
    text-align: center;
    line-height: 1;
  }
  
  #welcome-line-1 {
    color: #55ACEE;
    font-weight: 600;
    font-size: 40px;
  }
  
  #welcome-line-2 {
    color: #55ACEE;
    font-size: 18px;
    margin-top: 17px;
  }
  
  #input-area {
    margin-top: 40px;
  }
  
  .form-inp {
    padding: 11px 25px;
    background: transparent;
    border: 1px solid #e3e3e3;
    line-height: 1;
    border-radius: 8px;
  }
  
  .form-inp:focus-within {
    border: 1px solid #55ACEE;
  }
  
  .form-inp:not(:last-child) {
    margin-bottom: 15px;
  }
  
  .form-inp input {
    width: 100%;
    background: none;
    font-size: 13.4px;
    color: #55ACEE;
    border: none;
    padding: 0;
    margin: 0;
  }
  
  #submit-button-cvr {
    margin-top: 20px;
  }
  
  #submit-button {
    display: block;
    width: 100%;
    color: #55ACEE;
    background-color: transparent;
    font-weight: 600;
    font-size: 14px;
    margin: 0;
    padding: 14px 13px 12px 13px;
    border: 0;
    outline: 1px solid #55ACEE;
    border-radius: 8px;
    line-height: 1;
    cursor: pointer;
    transition: all ease-in-out .3s;
  }
  
  #submit-button:hover {
    background-color: #55ACEE;
    color: #161616;
  }
  
  #forgot-pass {
    text-align: center;
    margin-top: 10px;
  }
  
  #forgot-pass a {
    color: #868686;
    font-size: 12px;
    text-decoration: none;
  }
  </style>
  