import React from 'react';
import {Route} from 'react-router-dom'
import './App.css';
import Hangman from './components/hangman.js'
import Login from './components/login.js'
import HomePage from './components/HomePage.js'
import PhraseForm from './components/PhraseForm.js'
import FriendsList from './components/FriendList.js'

function App() {
  return (
    <div>
      <Route 
        exact path = '/login'
        component = {Login}
      />
      <Route 
        exact path = '/homepage'
        component = {HomePage}
      />
      <Route 
        exact path = '/play_game'
        component = {Hangman}
      />
      <Route 
        exact path = '/phrase'
        component = {PhraseForm}
      />
      <Route
      exact path = '/friends_list'
      component = {FriendsList}
      />
    </div>
  );
}

export default App;
