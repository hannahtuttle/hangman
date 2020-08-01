import React, {useEffect, useState} from 'react'
// import axios from 'axios'
import {Link} from 'react-router-dom'
// import {setPusherClient} from 'react-pusher'
import Pusher from 'pusher-js'
import * as PusherTypes from 'pusher-js'


const FriendList = () => {
    const [friends, setFriends] = useState([])

    let id = localStorage.getItem('id')
    console.log('id :', id)

    // const friends = []
    // console.log(process.env.REACT_APP_APP_KEY)
    const pusherClient = new Pusher(
        process.env.REACT_APP_APP_KEY,{
        cluster: process.env.REACT_APP_APP_CLUSTER,
        authEndpoint: `http://127.0.0.1:5000/pusher/auth/${id}`,
    })

    let channel = pusherClient.subscribe('multiplayer-hangman')
    channel.bind('my-event', function(data) {
        console.log('data', data)
        alert('An event was triggered with message: ' + data.message);
    });
    let presenceChannel = pusherClient.subscribe('presence-multiplayer-game')
    console.log(presenceChannel)
    console.log(presenceChannel.members.members)
    presenceChannel.bind('pusher:subscription_succeeded', (player) => {
        // this.players = player.count - 1
        console.log('player', player)
        // let me = presenceChannel.members.me.id
        player.each(member => {
            console.log('member', member)
              if (member.id != player.me.id){
                console.log('test rendering all players')
                // console.log('players', player.id)
                // friends.push(member.id)
                setFriends([...friends, member.id])
                console.log('friends', friends)
              }else if(player.count < 2){
                  console.log('there are no other players online')
              }
    
        })
    });
      
  

    return (
        <>
        {console.log('friends out of bind', friends)}
        <h1>Available friends</h1>
        {friends.map(player => {
            console.log('attempting to render players')
           return <Link to={{pathname:'/phrase', /*state: {player2_id: player.id}*/}}><p key = {player}>{player}</p></Link>
        })}
        </>
    )
}

export default FriendList;