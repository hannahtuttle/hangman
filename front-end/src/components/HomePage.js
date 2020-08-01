import React, {useState} from 'react'
import Title from './Title.js'
import FriendsList from './FriendList.js'
import axios from 'axios'
import {Link} from 'react-router-dom'

const HomePage = (props) => {

    const [gameId, setGameId] = useState(0)

    const playerId = localStorage.getItem('id')


    return (
        <div>
            <Title/>
            <Link to={'/friends_list'}>
            <button>Play with a friend</button>
            </Link>
            <Link to ={{pathname: '/play_game', state: props.history.location.pathname }}>
                <button>Play the game</button> 
            </Link>
        </div>
    )
}

export default HomePage;