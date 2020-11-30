import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import Swiper from 'react-native-deck-swiper';
import { Card } from '../components/card.js';

export class SwipeScreen extends React.Component {

    constructor(props){
      super(props);
      this.state = {
        category: 'General',
        cards: ['UT administration approves modified pass/fail expansion for fall 2020, spring 2021',
                'Among Us Tournament\nTuesday, Dec 1 at 7pm',
                'No. 13 Iowa State 23, No. 17 Texas 20: ‘Wish it didn’t have to go this way’',
                '@UTAustin will increase rent for new residents at three University-owned apartment complexes by an average of 41%.',
                '@AustinFC uniforms coming 12.18',
                '5',
                '6',
                '7',
                '8',
                ''],
        sources: ['Twitter', 'HornsLink', 'News', 'News', 'Twitter', 'HornsLink', 'News', 'Twitter', 'HornsLink', 'Twitter'],
        sourceText: ['@TheDailyTexan', 'HornsLink', 'Austin-American Statesman', 'The Daily Texan', '@McConaughey', 'HornsLink', 'KXAN', '@SamEhlinger', 'HornsLink', '@UTAustin'],
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
            stackSize={5}
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