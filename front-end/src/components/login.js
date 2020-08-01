import React, {useState} from 'react'
import axios from 'axios'


const Login = (props) => {

    const [user, setUser] = useState({username: '', password: ''})

    let handleChange = (event) => {
        setUser({...user, [event.target.name]: event.target.value})
    }

    let handleSubmit = (event) => {
        event.preventDefault()
        axios.post('http://127.0.0.1:5000/sign_up', {user})
        .then(res => {
            localStorage.setItem('id', res.data.user_id)
            console.log(res)
            props.history.push('/homepage')
        })
        .catch(err => console.log(err))
        //if account exists redirect to homepage
    }

    return (
        <div>
            <h1>Put in your details to play...</h1>
            <form onSubmit = {handleSubmit}>
                <label>Username :</label>
                <input
                type = 'text'
                name = 'username'
                value = {user.username}
                placeholder = ''
                onChange = {handleChange}
                />
                <label>Email :</label>
                <input
                 type = 'text'
                 name = 'password'
                 value = {user.password}
                 placeholder = ''
                 onChange = {handleChange}
                />
                <button>Login</button>
            </form>
        </div>
    )
}

export default Login;