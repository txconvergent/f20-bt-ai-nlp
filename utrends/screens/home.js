import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import Swiper from 'react-native-deck-swiper';

export class HomeScreen extends React.Component {

    constructor(props){
      super(props);
      this.state = {
        cards: ['PLACEHOLDER 0', '1', '2', '3', '4', '5', '6', '7', '8', ''],
        cardIndex: 0,
      };
    }
  
    renderCard = (card) => {
      return (
        <View style={styles.card}>
          <Text style={styles.cardText}>{card}</Text>
        </View>
      )
    }
  
    onSwiped = (cardIndex) => {
      this.swiper.jumpToCardIndex(0)
      console.log("UPDATING CARDS")
      if (cardIndex == 8) {
        const newCards = this.getNewCards();
        this.setState({
          cards: newCards
        })
      }
    }
  
    getNewCards = () => {
      return ['NEW0', 'NEW1', 'NEW2', 'NEW3', 'NEW4', 'NEW5', 'NEW6', 'NEW7', 'NEW8', 'NEW9']
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
  
  card: {
    flex: 1,
    borderRadius: 15,
    borderWidth: 2,
    borderColor: "#E8E8E8",
    justifyContent: "center",
    backgroundColor: "#19297C",
  },

  cardText: {
    textAlign: "center",
    fontSize: 50,
    backgroundColor: "transparent",
    color: 'white'
  },
});