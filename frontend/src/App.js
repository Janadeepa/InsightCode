import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Dashboard from './components/Dashboard';
import ReviewList from './components/ReviewList';
import CodeReview from './components/CodeReview';
import './styles/App.css';

function App() {
    return (
        <Router>
            <div className="App">
                <Switch>
                    <Route path="/" exact component={Dashboard} />
                    <Route path="/reviews" component={ReviewList} />
                    <Route path="/review/:id" component={CodeReview} />
                </Switch>
            </div>
        </Router>
    );
}

export default App;
