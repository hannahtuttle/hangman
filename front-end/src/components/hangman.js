import React from 'react'
import './hangman.css'


const Hangman = () => {

    const alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    const samplePhrase = 'hello my name is Hannah'

    const ConvertToSpaces = () => {
        let hiddenPhrase = []
        for (const letter of samplePhrase){
            if (letter != ' '){
                hiddenPhrase.push('_')
            }else {
                hiddenPhrase.push(' ')
            }
        }
        return hiddenPhrase
    }

    ConvertToSpaces()

    return (
        <div>
            
            <div className = 'top'></div>
            <div className = 'fit'>
                <div>
                    <div className = 'rope'></div>
                    <div className = 'head'></div>
                    <div className = 'body_configuration'> 
                        <div className = 'arm_2'></div>
                        <div className = 'body'></div>
                        <div className = 'arm_1'></div>
                    </div>
                        <div className = 'leg_1'></div>
                        <div className = 'leg_2'></div>
                </div>
                <div className = 'pole'></div>
            </div>
            <div className = 'base'></div>

            <div>

            </div>


            {alphabet.map(letter => <button className="button" key = {letter}>{letter}</button>)}
        </div>
    )
}

export default Hangman;