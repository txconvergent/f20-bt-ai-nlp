import 'react-native-gesture-handler';
import React from 'react';
import { StyleSheet, Text, View, Image } from 'react-native';


export const ProfilePage = () => {
    return(
        <View>
            <View style={styles.container}>
                <TopBar style = {button_styles.container} />
                <Text style = {text_styles.container}>Profile </Text>
                <ProfileImage />
            </View>
            <Text style = {{marginLeft: 5 + 'em'}}><b>Saved Posts: </b> </Text>
        </View>
        
    )
}

export const ProfileImage = () => {
    return(
      <Image source = {{
            width: 200,
            height: 200,
            uri: "https://i.imgur.com/1e039tU.png"
        }}/>
    )
  }

  export const TopBar = () => {
      return(
        <button style = {{
            color: 'darkBlue',
            borderRadius: 8,
            marginLeft: 10 + 'em',
            backgroundColor: '#FFF',
            borderColor: 'darkBlue'
        }}
        
        href = '#'>
            Edit Profile
        </button>
      )
  }

  export const DummyPosts = () =>{
      return(
        <text>
          hi
        </text>
      )

  }

  const text_styles = StyleSheet.create({
    container: {
      fontSize: 30
    }
  });

  const button_styles = StyleSheet.create({
      button: {
        color: 'red'
      }
  })

  const styles = StyleSheet.create({
    container: {
      flex: 1,
      backgroundColor: '#FFFFFF',
      alignItems: 'center',
      justifyContent: 'center',
    },
  });