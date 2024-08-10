import React, { useEffect, useState } from 'react';

function ReviewList() {
    const [reviews, setReviews] = useState([]);

    useEffect(() => {
        // Fetch review data from backend API
        fetch('/api/reviews')
            .then(response => response.json())
            .then(data => setReviews(data));
    }, []);

    return (
        <div className="review-list">
            <h2>Pull Request Reviews</h2>
            <ul>
                {reviews.map(review => (
                    <li key={review.id}>
                        <h3>{review.title}</h3>
                        <p>{review.summary}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default ReviewList;
