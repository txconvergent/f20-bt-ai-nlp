import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { createMaterialTopTabNavigator } from '@react-navigation/material-top-tabs';
import Swiper from 'react-native-deck-swiper'

function SettingsScreen() {
  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Text>Settings</Text>
    </View>
  );
}

function ProfileScreen() {
  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Text>Settings</Text>
    </View>
  );
}

class HomeScreen extends React.Component {

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

function getCard() {
  return (
    <View style={styles.card}>
      <Text style={styles.cardText}>{Math.random()}</Text>
    </View>
  )
}

function SearchScreen() {
  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Text>Search</Text>
    </View>
  );
}

function SavedScreen() {
  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Text>Saved stories</Text>
    </View>
  );
}

const Tab = createBottomTabNavigator();

export default function App() {
  return (
    <>
    <NavigationContainer>
      <Tab.Navigator>
        <Tab.Screen name="Home" component={HomeScreen} />
        <Tab.Screen name="Search" component={SearchScreen} />
        <Tab.Screen name="Saved" component={SavedScreen} />
      </Tab.Navigator>
    </NavigationContainer>
    </>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: 'white',
    alignItems: 'center',
    justifyContent: 'center',
  },

  card: {
    flex: 1,
    borderRadius: 15,
    borderWidth: 2,
    borderColor: "#E8E8E8",
    justifyContent: "center",
    backgroundColor: "#19297c"
  },

  cardText: {
    textAlign: "center",
    fontSize: 50,
    backgroundColor: "transparent",
    color: 'white'
  },
});
