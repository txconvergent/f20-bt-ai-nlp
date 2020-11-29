import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import Swiper from 'react-native-deck-swiper';
import { Card } from '../components/card.js';

export class HomeScreen extends React.Component {

    constructor(props){
      super(props);
      this.state = {
        category: 'General',
        cards: ['This is a significant amount of text lol how much can we fit', '1', '2', '3', '4', '5', '6', '7', '8', ''],
        sources: ['Twitter', 'HornsLink', 'News', 'News', 'Twitter', 'HornsLink', 'News', 'Twitter', 'HornsLink', 'Twitter'],
        sourceText: ['@DailyTexan', 'HornsLink', 'Austin-American Statesman', 'Daily Texan', '@McconaugheyOfficial', 'HornsLink', 'KXAN', '@SamEhlinger', 'HornsLink', '@UTAustin'],
        cardIndex: 0,
      };
    }
  
    renderCard = (cardText, cardIndex) => {
      return (
        <Card text={cardText} category={this.state.category} source={this.state.sources[cardIndex]} sourceText={this.state.sourceText[cardIndex]}/>
      )
    }
  
    onSwiped = (cardIndex) => {
      if (cardIndex == 8) {
        const newCards = this.getNewCards();
        this.setState({
          cards: newCards
        })
      }
    }
  
    getNewCards = () => {
      return ['New 0', 'New 1', 'New 2', 'New 3', 'New 4', 'New 5', 'New 6', 'New 7', 'New 8', 'New 9']
    }
  
    render() {
      return (
        <View style={styles.container}>
          <Swiper
            ref={swiper => {
              this.swiper = swiper
            }}
            onSwiped={this.onSwiped}
            cards={this.state.cards}
            cardIndex={0}
            cardVerticalMargin={80}
            renderCard={this.renderCard}

            infinite={true}
            backgroundColor={'white'}
            stackSize={2}
            />
        </View>
      )
    }
}

const styles = StyleSheet.create({
  container: {
    alignItems: 'stretch',
    position: 'absolute',
    top: "-10%",
    left: 0,
    right: 0,
    bottom: 0,
    backgroundColor: 'white',
  },
});