import React from 'react';

export default function Home({ onRouteChange,user }) {

    return (
        <div className="ml3">
            <div className="lh-copy mt3 tr mr4 underline">
                <p
                    onClick={() => onRouteChange('signin')}
                    className="f3 link dim black db pointer"
                >
                    {'Sign out'}
                </p>
            </div>
            <h2>Home page</h2>
            <div>Logged in Successfully......</div>
            {/* <p>Id : {user.id}</p> */}
            <p>Hello {user.name}</p>
            <p>Email : {user.email}</p>
        </div>
    )
}