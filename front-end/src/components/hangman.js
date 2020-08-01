import React, {useEffect, useState} from 'react'
import axios from 'axios'
import './hangman.css'
import FriendsList from './FriendList.js'


const Hangman = (props) => {

    // const [count, setCount] = useState(0)
    const alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    const playerId = localStorage.getItem('id')
    // console.log('previous path', props.history.location.state)
    const previousPath = props.history.location.state
    const [phrase, setPhrase] = useState('')
    // let samplePhrase = 'hello my name is hannah'

    
// useEffect(() => {
//       console.log("*****************is this working*******************")
//         console.log('path', previousPath)
//         if(previousPath == '/homepage'){
//             const fake_player = 9
//             const testId = 3
//             console.log('************test run*****************')
//             axios.post('http://127.0.0.1:5000/start_game', {player_1 : testId, player_2: fake_player})
//             .then(res => {
//                 console.log(res.data) 
//                 axios.get(`http://127.0.0.1:5000//guess_phrase/${res.data}`)
//                 .then(response => {setPhrase(response.data)})
//             })
//             .catch(err => console.log('error', err))
//         } else {
//             const send_phrase = props.history.location.state
//             console.log('send phrase', send_phrase)
//             axios.post('http://127.0.0.1:5000/give_phrase', {send_phrase})
//             .then(res => {
//             console.log(res.data.game_id) 
//             axios.get(`http://127.0.0.1:5000//guess_phrase/${res.data.game_id}`)
//                 .then(response => {
//                     console.log(response)
//                     setPhrase(response.data.phrase1)
//                 })
//             })
//             .catch(err => console.log(err))
//         }
// }, [])



    
    
    let hiddenPhrase = []
    
    const ConvertToSpaces = (phr) => {
        for (const letter of phr){
            if (letter !== ' '){
                hiddenPhrase.push(letter)
            }else {
                hiddenPhrase.push(' ')
            }
        }
    }
    
    ConvertToSpaces(phrase)
    const table = {}
    for (let i = 0; i < hiddenPhrase.length; i++){

        if(!table[hiddenPhrase[i]]){
            table[hiddenPhrase[i]] = [i]
        }else{
            table[hiddenPhrase[i]].push(i)
        }
    }
    
    const [correctGuess, setCorrectGuess] = useState([])
    const [incorrectGuess, setIncorrectGuess] = useState([])
    

    const checkLetter = (e) => {
        e.preventDefault()
        console.log('letter', e.target.value)
       if(table[e.target.value]){
           setCorrectGuess([...correctGuess, e.target.value]) 
       }else {
           setIncorrectGuess([...incorrectGuess, e.target.value])
            // setCount(incorrectGuess.length)
       }
        console.log('correctGuess',correctGuess)
        console.log('incorrectGuess length',incorrectGuess.length)
    
    }
 

    return (
        <div>
            
            <div className = {incorrectGuess.length > 2 ? 'top': 'top_hidden'}></div>
            <div className = 'fit'>
                <div>
                    <div className = {incorrectGuess.length > 3 ?'rope': 'rope_hidden'}></div>
                    <div className = {incorrectGuess.length > 4 ? 'head': 'head_hidden'}></div>
                    <div className = 'body_configuration'> 
                        <div className = {incorrectGuess.length > 6 ? 'arm_2': 'arm_2_hidden'}></div>
                        <div className = {incorrectGuess.length > 5 ? 'body': 'body_hidden'}></div>
                        <div className = {incorrectGuess.length > 7 ? 'arm_1': 'arm_1_hidden'}></div>
                    </div>
                        <div className = {incorrectGuess.length > 8 ? 'leg_1': 'leg_1_hidden'}></div>
                        <div className = {incorrectGuess.length > 9 ?'leg_2': 'leg_2_hidden'}></div>
                </div>
                <div className = {incorrectGuess.length > 1 ? 'pole': 'pole_hidden'}></div>
            </div>
            <div className = {incorrectGuess.length > 0 ? 'base': 'base_hidden'}></div>

            <div className = 'spaces'>
                {hiddenPhrase.map(space => {
                    if(correctGuess.includes(space)){
                    return <div className = 'space'>{space}</div>
                    }
                return <div className='show'
                >{space}</div>

                })}
            </div>

            {alphabet.map(letter => <button 
            className= {correctGuess.includes(letter) || incorrectGuess.includes(letter) ? 'button_clicked':"button" }
            key = {letter}
            value = {letter}
            onClick = {checkLetter}
            >{letter}</button>)}

            <FriendsList/>
        </div>
    )
}

export default Hangman;