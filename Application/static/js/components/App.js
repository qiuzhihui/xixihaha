import React from 'react'
import AppFooter from './Footer'
import AddTodo from '../containers/AddTodo'
import VisibleTodoList from '../containers/VisibleTodoList'
import Header from './Header'
import ControlledCarousel from './ControlledCarousel'
import MainPage from './MainPage'

const App = () => (
  <div style={{'backgroundColor':'black'}}>
    <Header />
    <MainPage />
    <AppFooter />
  </div>
)

export default App