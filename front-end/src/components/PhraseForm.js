import React, {useState, useEffect} from 'react'
import axios from 'axios'
import {Link} from 'react-router-dom'


const PhraseForm = (props) => {
    
    const testId = 4
    const [phrase, setPhrase] = useState({phrase: '', game_id: '', player_id: testId})

    const player2 = props.history.location.state
    console.log(player2)
    useEffect(() => {
        axios.post('http://127.0.0.1:5000/start_game', {player_1 : testId, player_2: player2.player2_id})
        .then(res => {
            setPhrase({...phrase, game_id: res.data.game_id})
            console.log(res)
        })
        .catch(err => console.log(err))
    }, [])
    
    const handleChange = (event) => {
        setPhrase({...phrase, phrase: event.target.value})
    }

    const handleSubmit = (event) => {
        event.preventDefault()
        // axios.post('http://127.0.0.1:5000/give_phrase', {phrase})
        // .then(res => {
        //    console.log(res) 
        // })
        // .catch(err => console.log(err))
    }

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <label>Write a word or a phrase for your friend here:</label>
                <textarea
                type = 'text'
                name = 'phrase'
                value = {phrase.phrase}
                placeholder = ''
                onChange = {handleChange}
                />
                <Link to={{pathname:'/play_game', state : phrase}}><button type='submit'> Start Game</button></Link>
            </form>
        </div>
    )

}

export default PhraseForm;