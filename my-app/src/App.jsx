import{BrowserRouter,Routes,Route} from 'react-router-dom'
import Home from './Home.jsx'
import Viewer from './Viewer.jsx'

export default function App(){
  return(
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Home/>}/>
        <Route path='/viewer/:docId' element={<Viewer/>}/>
      </Routes>
    </BrowserRouter>
  )
}