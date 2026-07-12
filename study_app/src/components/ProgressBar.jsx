import React from 'react';

export default function ProgressBar({ total, current, completed }) {
  return (
    <div className="progress-bar">
      {Array.from({ length: total }).map((_, i) => {
        let cls = 'progress-dot';
        if (completed.has(i)) cls += ' completed';
        else if (i === current) cls += ' current';
        return <div key={i} className={cls} />;
      })}
    </div>
  );
}
