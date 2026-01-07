import { useParams } from "react-router-dom";
import './App.css'
import { useEffect, useState } from "react";
const BACKEND="http://localhost:5000";

export default function Viewer() {
    const { docId } = useParams()
    const [page, setPage] = useState(1);

    return(
     <div style={{ padding: 20 }}>
      <h2>Viewing PDF: {docId}</h2>

      <img
        src={`${BACKEND}/api/pdf/${docId}/page/${page}`}
        style={{ maxWidth: "100%" }}
      />

      <div style={{ marginTop: 10 }}>
        <button disabled={page === 1} onClick={() => setPage(p => p - 1)}>
          Prev
        </button>
        <button onClick={() => setPage(p => p + 1)}>
          Next
        </button>
      </div>
    </div>

    )}