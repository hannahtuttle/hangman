import React, {useState, useEffect} from 'react'




const SignUp = () => {
    const [signUp, setSignUp] = useState({username: '', password: ''})

    let handleChange = (event) => {
        setSignUp({...signUp, [event.target.name]: event.target.value})
    }

    let handleSubmit = (event) => {
        event.preventDefault()
        //send to backend
        //if correctly made redirect to homepage
    }

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <label>Username :</label>
                <input
                type = 'text'
                name = 'username'
                value = {event.target}
                placeholder = ''
                onChange = {handleChange}
                />
                <label>Password :</label>
                <input
                 type = 'text'
                 name = 'password'
                 value = {event.target}
                 placeholder = ''
                 onChange = {handleChange}
                />
                <button>Sign Up</button>
            </form>
        </div>
    )
}

export default SignUp;