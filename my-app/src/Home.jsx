import { useNavigate } from 'react-router-dom';
import pdfIcon from './assets/pdf.png'
import './App.css'


function App() {
    const navigate = useNavigate();
  const openPdf = (docId) => {
    navigate(`/viewer/${docId}`);
  }
 

  return (<> <h1 class="card">PDF Documents</h1>
    <div class="grid">
        <div class="card">
            <img src={pdfIcon} alt="PDF Icon 1"/>
            <button onClick={() => openPdf('1')}>Open PDF 1</button>
        </div>
        <div class="card">
            <img src={pdfIcon} alt="PDF Icon 2"/>
            <button onClick={() => openPdf('2')}>Open PDF 2</button>
        </div>
        <div class="card">
            <img src={pdfIcon} alt="PDF Icon 3"/>
            <button onClick ={() => openPdf('3')}>Open PDF 3</button>
        </div>
        <div class="card">
            <img src={pdfIcon} alt="PDF Icon 4"/>
            <button onClick={() => openPdf('4')}>Open PDF 4</button>
        </div>
    </div> 
  </>
  
  )
}

export default App
