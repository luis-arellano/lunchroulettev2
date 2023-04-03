import React, { useState } from "react";

import { GoogleLogin } from "react-google-login";
import FacebookLogin from "react-facebook-login";
import apiService from "../apiService";

function Login() {
  const [isLogin, setIsLogin] = useState(true);

  const responseGoogle = (response) => {
    console.log(response);
  };

  const responseFacebook = (response) => {
    console.log(response);
  };

  const handleSubmit = async (event) => {
    console.log("event: ", event);
    console.log("API: ", process.env.REACT_APP_API_BASE_URL);
    event.preventDefault();
    // Handle login or sign up logic here
    const userData = {
      name: event.target.name.value,
      email: event.target.email.value,
      password: event.target.password.value,
    };

    // Create User via API
    try {
      const result = await apiService.createUser(userData);
      console.log("RESULT: ", result);
    } catch (error) {
      console.error("Error creating user:", error.message);
    }
  };

  return (
    <div className="max-w-md mx-auto flex flex-col py-8 px-4 space-y-4 bg-white rounded-xl shadow-xl">
      <h2 className="text-3xl font-semibold text-gray-800">Lunch Roulette</h2>
      <p> Matchmaker</p>
      <br></br>
      <div>
        <GoogleLogin
          clientId="YOUR_CLIENT_ID"
          buttonText="Sign in with Google"
          onSuccess={responseGoogle}
          onFailure={responseGoogle}
          cookiePolicy={"single_host_origin"}
          className="w-full flex justify-center bg-white border border-gray-300 rounded-md shadow-sm py-2 px-4 text-sm font-medium  text-gray-700 hover:bg-gray-50"
        />
      </div>
      <div>
        <FacebookLogin
          appId="YOUR_APP_ID"
          fields="name,email,picture"
          callback={responseFacebook}
          cssClass="w-full flex justify-center bg-white border border-gray-300 rounded-md shadow-sm py-2 px-4 text-sm font-medium  text-gray-700 hover:bg-gray-50"
          icon={
            <svg
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 24 24"
              fill="#1877f2"
              width="20"
              height="20"
              className="mx-5"
            >
              <path d="M21.5 0h-19C1.673 0 .01 1.673.01 3.75L0 20.25c0 2.076 1.673 3.75 3.75 3.75h19c2.076 0 3.75-1.673 3.75-3.75V3.75c0-2.077-1.674-3.75-3.75-3.75zm-3.937 7.5h-1.473c-.639 0-.888.3-.888.813v1.063h2.738l-.363 2.775h-2.375v7.313h-3.188v-7.313h-1.9v-2.775h1.9V7.163c0-1.888 1.175-2.913 2.813-2.913h1.537v2.25z" />
            </svg>
          }
        />
      </div>
      <div class="bg-gray z-1">or</div>

      <form onSubmit={handleSubmit} className="space-y-6">
        {!isLogin && (
          <div>
            <div className="mt-1">
              <input
                id="name"
                name="name"
                type="text"
                placeholder="Full Name"
                autoComplete="name"
                required
                className="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
              />
            </div>
          </div>
        )}
        <div>
          <div className="mt-1">
            <input
              id="email"
              name="email"
              type="email"
              placeholder="Email Address"
              autoComplete="email"
              required
              className="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
            />
          </div>
        </div>
        <div>
          <div className="mt-1">
            <input
              id="password"
              name="password"
              type="password"
              placeholder="Password"
              autoComplete="new-password"
              required
              className="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
            />
          </div>
        </div>
        {!isLogin && (
          <div>
            <div className="mt-1">
              <input
                id="confirm-password"
                name="confirm-password"
                type="password"
                placeholder="Confirm Password"
                autoComplete="new-password"
                required
                className="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
              />
            </div>
          </div>
        )}
        <div className="flex items-center justify-between">
          <div className="flex items-center">
            <input
              id="remember-me"
              name="remember-me"
              type="checkbox"
              className="h-4 w-4 text-indigo-600 focus:ring-indigo-500 border-gray-300 rounded"
            />
            <label
              htmlFor="remember-me"
              className="ml-2 block text-sm text-gray-900"
            >
              Remember me
            </label>
          </div>
          {isLogin && (
            <div className="text-sm">
              <a
                href="#"
                className="font-medium text-indigo-600 hover:text-indigo-500"
              >
                Forgot your password?
              </a>
            </div>
          )}
        </div>
        <div>
          <button
            type="submit"
            className="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
          >
            {isLogin ? "Log In" : "Sign Up"}
          </button>
        </div>
      </form>
      <div className="text-center">
        <span>
          {isLogin ? "Don't have an account?" : "Already have an account?"}{" "}
        </span>
        <button
          className="font-medium text-indigo-600 hover:text-indigo-500"
          onClick={() => setIsLogin(!isLogin)}
        >
          {isLogin ? "Sign up" : "Log in"}
        </button>
      </div>
    </div>
  );
}

export default Login;
