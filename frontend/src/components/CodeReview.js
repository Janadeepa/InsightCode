import React from 'react';

function CodeReview({ review }) {
    return (
        <div className="code-review">
            <h2>{review.title}</h2>
            <pre>{review.code}</pre>
            <p><strong>Feedback:</strong> {review.feedback}</p>
        </div>
    );
}

export default CodeReview;
